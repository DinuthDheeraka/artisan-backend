from starlette.responses import JSONResponse

from app.db.session import SessionLocal
from app.exceptions.exceptions import ApplicationServiceException
from app.models.models import Buyer, Orders, Artwork, OrderDetail, Artist


async def save_order(order_data):
    with SessionLocal() as session:
        try:
            # check if buyer is existing
            buyer = session.query(Buyer).filter_by(id=order_data.buyer_id, buyer_status='ACTIVE').first()

            # if buyer not existing.. raise exp
            if buyer is None:
                raise ApplicationServiceException(200, False, 'buyer not found')

            # save order
            order = Orders(buyer_id=buyer.id)
            session.add(order)

            # Flush the session to ensure the order.id is populated
            session.flush()

            for item in order_data.cart:
                # find artwork by id
                artwork = session.query(Artwork).filter_by(id=item['item_id']).first()

                current_copies = artwork.number_of_copies_for_sale
                order_qty = item['qty']

                if (current_copies - order_qty) < 0:
                    raise ApplicationServiceException(200, False, f"Artwork {item['title']} is already sold out.")

                # add order detail
                new_order_detail = OrderDetail(price=artwork.price_without_shipping, qty=item['qty'], order_id=order.id,
                                               artwork_id=artwork.id)
                session.add(new_order_detail)

                # update artwork
                artwork.number_of_copies_for_sale = current_copies - order_qty

                if (current_copies - order_qty) == 0:
                    artwork.sales_status = 'Sold'

                session.add(artwork)

            # Commit the changes
            session.commit()

            return {"status_code": 200, "success": True, "message": "Checkout successful"}

        except ApplicationServiceException as ae:
            session.rollback()
            return JSONResponse(status_code=ae.code,
                                content={"success": ae.success, "status_code": ae.code, "message": ae.message})

        except Exception as ae:
            session.rollback()
            return JSONResponse(status_code=500,
                                content={"success": False, "status_code": 200, "message": "Exception in save_order"})


async def get_orders_by_buyer_id(buyer_id):
    with SessionLocal() as session:
        try:
            data = []

            orders = session.query(OrderDetail).join(Orders, OrderDetail.order_id == Orders.id).filter_by(
                buyer_id=buyer_id).all()

            for i in range(len(orders)):
                order_detail = orders[i]

                artwork = session.query(Artwork).filter_by(id=order_detail.artwork_id).first()

                artist = session.query(Artist).filter_by(id=artwork.artist_id).first()

                data.append({"id": order_detail.id, "price": order_detail.price, "qty": order_detail.qty,
                             "date": order_detail.created_at, "artwork_id": artwork.id, "artwork_name": artwork.title,
                             "artist_id": artist.id, "artist_name": artist.display_name,
                             "artwork_img": artwork.main_image})

            return data

        except Exception as e:
            session.rollback()
            raise e
