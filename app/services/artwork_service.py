from datetime import datetime

from app.db.session import SessionLocal
from app.exceptions.exceptions import ApplicationServiceException
from app.ml.nsfw_text_detector import detect_text
# from app.ml.nsfw_text_detector import detect_text
from app.models.models import Artwork, Artist, Buyer, Review
from app.util.s3_file_uploader import upload_to_s3


async def save_artwork(artwork_data):
    with SessionLocal() as session:
        try:

            # upload profile image
            object_name = (f"uploads/artworks/{datetime.utcnow()}{'_'}"
                           f"{artwork_data.main_image.filename}")

            main_img_url = upload_to_s3(object_name, artwork_data.main_image.file)

            new_artwork = Artwork(title=artwork_data.title, year_of_creation=artwork_data.year_of_creation,
                                  artwork_category=artwork_data.artwork_category, medium=artwork_data.medium,
                                  support_or_surface=artwork_data.support_surface,
                                  number_of_copies=artwork_data.number_of_copies,
                                  number_of_copies_for_sale=artwork_data.number_of_copies_for_sale,
                                  main_image=main_img_url, can_display_outdoors=artwork_data.can_display_outdoor,
                                  can_display_on_walls=artwork_data.can_display_on_wall,
                                  ready_to_hang=artwork_data.ready_to_hang, is_framed=artwork_data.is_framed,
                                  frame_height=artwork_data.frame_height, frame_width=artwork_data.frame_width,
                                  frame_thickness=artwork_data.frame_thickness, height=artwork_data.height,
                                  width=artwork_data.width, thickness=artwork_data.thickness,
                                  weight=artwork_data.weight, sales_status=artwork_data.sales_status,
                                  price_without_shipping=artwork_data.price_without_shipping,
                                  discount_price=artwork_data.discount_price,
                                  artwork_condition=artwork_data.artwork_condition,
                                  description=artwork_data.description, artwork_style=artwork_data.artwork_style,
                                  keywords=artwork_data.keywords, artist_id=artwork_data.artist_id)

            session.add(new_artwork)

            session.commit()

        except Exception as e:
            session.rollback()
            raise e


async def get_all_artworks(category, artist_name, style, min_price, max_price):
    with (SessionLocal() as session):
        try:

            selected_fields = []

            if category != "" and artist_name == "" and style == "" and min_price == "" and max_price == "":
                print(1)
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.artwork_category == category, Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name != "" and style == "" and min_price == "" and max_price == "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.artwork_category == category, Artist.display_name == artist_name,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name != "" and style != "" and min_price == "" and max_price == "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.artwork_category == category, Artist.display_name == artist_name,
                    Artwork.artwork_style == style, Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name != "" and style != "" and min_price != "" and max_price == "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price), Artwork.artwork_category == category,
                    Artist.display_name == artist_name, Artwork.artwork_style == style,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name != "" and style != "" and min_price != "" and max_price != "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price),
                    Artwork.price_without_shipping <= float(max_price), Artwork.artwork_category == category,
                    Artist.display_name == artist_name, Artwork.artwork_style == style,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name == "" and style != "" and min_price != "" and max_price != "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price),
                    Artwork.price_without_shipping <= float(max_price), Artwork.artwork_category == category,
                    Artist.display_name == artist_name, Artwork.artwork_style == style,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name == "" and style != "" and min_price != "" and max_price == "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price), Artwork.artwork_category == category,
                    Artwork.artwork_style == style, Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name == "" and style != "" and min_price == "" and max_price == "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.artwork_category == category, Artwork.artwork_style == style,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name == "" and style != "" and min_price == "" and max_price != "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(

                    Artwork.price_without_shipping <= float(max_price), Artwork.artwork_category == category,
                    Artwork.artwork_style == style, Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name == "" and style == "" and min_price != "" and max_price != "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price),
                    Artwork.price_without_shipping <= float(max_price), Artwork.artwork_category == category,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name == "" and style == "" and min_price != "" and max_price == "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price), Artwork.artwork_category == category,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category != "" and artist_name == "" and style == "" and min_price == "" and max_price != "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(

                    Artwork.price_without_shipping <= float(max_price), Artwork.artwork_category == category,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name == "" and style == "" and min_price == "" and max_price != "":
                pass

            # --------------------------------------------------------------------------------------------------

            if category == "" and artist_name != "" and style != "" and min_price != "" and max_price != "":
                print("all")
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price),
                    Artwork.price_without_shipping <= float(max_price), Artist.display_name == artist_name,
                    Artwork.artwork_style == style, Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name != "" and style != "" and min_price != "" and max_price == "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price), Artist.display_name == artist_name,
                    Artwork.artwork_style == style, Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name != "" and style != "" and min_price == "" and max_price == "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(

                    Artist.display_name == artist_name, Artwork.artwork_style == style,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name != "" and style == "" and min_price == "" and max_price == "":
                print('artist')
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artist.display_name == artist_name, Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name != "" and style == "" and min_price != "" and max_price != "":
                print("all")
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price),
                    Artwork.price_without_shipping <= float(max_price), Artist.display_name == artist_name,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name != "" and style == "" and min_price != "" and max_price == "":
                print("all")
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price), Artist.display_name == artist_name,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name != "" and style == "" and min_price == "" and max_price != "":
                print("all")
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(

                    Artwork.price_without_shipping <= float(max_price), Artist.display_name == artist_name,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            # ------------------------------------------------------------------------------------------------

            if category == "" and artist_name == "" and style != "" and min_price != "" and max_price != "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price),
                    Artwork.price_without_shipping <= float(max_price), Artwork.artwork_style == style,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name == "" and style != "" and min_price != "" and max_price == "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price), Artwork.artwork_style == style,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name == "" and style != "" and min_price == "" and max_price != "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(

                    Artwork.price_without_shipping <= float(max_price), Artwork.artwork_style == style,
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name == "" and style != "" and min_price == "" and max_price == "":
                print('style')
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.artwork_style == style, Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            # ---------------------------------------------------------------------------------------------

            if category == "" and artist_name == "" and style == "" and min_price != "" and max_price != "":
                print("min-max-price")
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price),
                    Artwork.price_without_shipping <= float(max_price), Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name == "" and style == "" and min_price != "" and max_price == "":
                print("min-price")
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping >= float(min_price), Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name == "" and style == "" and min_price == "" and max_price != "":
                print("max-price")
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.price_without_shipping <= float(max_price), Artwork.artwork_status == 'ACTIVE',
                    Artwork.sales_status == 'For Sale').all()

            if category == "" and artist_name == "" and style == "" and min_price == "" and max_price == "":
                # Query the table and select only specific fields
                selected_fields = session.query(Artwork.id, Artwork.title, Artwork.price_without_shipping,
                                                Artwork.medium, Artwork.description, Artwork.height, Artwork.width,
                                                Artwork.thickness, Artwork.main_image, Artwork.length_unit,
                                                Artwork.artwork_category, Artist.full_name).join(Artist,
                                                                                                 Artwork.artist_id == Artist.id).filter(
                    Artwork.artwork_status == 'ACTIVE', Artwork.sales_status == 'For Sale').all()

            # Convert the results to a list of dictionaries
            results = [
                {"id": row.id, "title": row.title, "main_image": row.main_image, "price": row.price_without_shipping,
                 "medium": row.medium, "artist_name": row.full_name, "height": row.height, "width": row.width,
                 "category": row.artwork_category, "thickness": row.thickness, "unit": row.length_unit} for row in
                selected_fields]

            return {"selected_artworks": results}

        except Exception as e:

            session.close()
            raise ApplicationServiceException(True, 200, 'Exception in get_all_artworks')

        finally:
            session.close()


async def get_art_by_id(artwork_id: int):
    with (SessionLocal() as session):
        try:

            # find artwork by id
            artwork = session.query(Artwork).filter_by(id=artwork_id).first()

            # Query the table and select only specific fields
            artist_by_id = session.query(Artist.id, Artist.display_name, Artist.profile_img_url,
                                         Artist.biography).filter(Artist.id == artwork.artist_id).first()

            artist = {"id": artist_by_id.id, "display_name": artist_by_id.display_name,
                      "profile_img_url": artist_by_id.profile_img_url, "biography": artist_by_id.biography}

            return {"selected_artwork": artwork, "artist": artist}

        except Exception as e:

            session.close()
            raise ApplicationServiceException(True, 200, 'Exception in get_all_artworks')

        finally:
            session.close()


async def save_artwork_review(artwork_data):
    with SessionLocal() as session:
        try:
            # check if buyer is existing
            buyer = session.query(Buyer).filter_by(id=artwork_data.buyer_id, buyer_status='ACTIVE').first()

            # if buyer not existing.. raise exp
            if buyer is None:
                raise ApplicationServiceException(200, False, 'buyer not found')

            # find artist_id by artwork_id
            artwork = session.query(Artwork).filter_by(id=artwork_data.artwork_id).first()

            print(artwork_data.review_comment)

            sfw_score = detect_text(artwork_data.review_comment)

            if sfw_score[0]['label'] == 'NSFW':
                return {"status_code": 800, "success": False, "message": "Review comment is not safe for publish."}

            # upload profile image
            object_name = (f"uploads/review_images/{datetime.datetime.utcnow()}{'_'}"
                           f"{artwork_data.review_image.filename}")

            review_img_url = upload_to_s3(object_name, artwork_data.review_image.file)

            # save new buyer
            new_review = Review(buyer_id=artwork_data.buyer_id, artwork_id=artwork_data.artwork_id,
                                artist_id=artwork.artist_id, display_name=artwork_data.display_name,
                                review_img_url=review_img_url, email=artwork_data.email,
                                review_comment=artwork_data.review_comment, review_points=artwork_data.review_points)

            # save review
            session.add(new_review)

            session.commit()

            return {"status_code": 200, "success": True, "message": "Review published successfully."}

        except Exception as e:
            session.rollback()
            raise e


async def get_reviews_by_artwork_id(artwork_id: int):
    with (SessionLocal() as session):
        try:

            # find artwork by id
            reviews = session.query(Review).filter_by(artwork_id=artwork_id).all()

            # Convert the results to a list of dictionaries
            results = [
                {"id": row.id, "buyer_id": row.buyer_id, "artwork_id": row.artwork_id, "display_name": row.display_name,
                 "email": row.email, "review_comment": row.review_comment, "review_img_url": row.review_img_url,
                 "review_points": row.review_points, "review_starts": row.review_stars, "is_positive": row.is_positive,
                 "positive_rate": row.positive_rate} for row in reviews]

            return {"reviews": results}

        except Exception as e:

            session.close()
            raise ApplicationServiceException(True, 200, 'Exception in get_all_artworks')

        finally:
            session.close()
