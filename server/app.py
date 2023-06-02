# Remote library imports
from flask import Flask, request, make_response, session, abort, jsonify
from flask_restful import Resource
from werkzeug.exceptions import NotFound, Unauthorized
import json
import traceback



# Local imports
from config import app, api, db
from models import User, Resort, Comment

class Users(Resource):
    def post(self):
        form_json = request.get_json()
        new_user = User(
            name = form_json['name'],
            email = form_json['email']
        )
        db.session.add(new_user)
        db.session.commit()
        session['user.id'] = new_user.id
        # import ipdb; ipdb.set_trace()
        response = make_response(
            new_user.to_dict(),
            201
        )

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        response = make_response('',204)
        return response
api.add_resource(Logout, '/logout')


class AuthorizedSession(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session['user_id']).first()
            return make_response(user.to_dict(), 200)
        else:
            return {'message': '401: Not Authorized'}, 401

api.add_resource(AuthorizedSession, '/authorized')

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('name')
        password = data.get('password')
        user = User.query.filter_by(name=username).first()
        if user:
            if user.authenticate(password):
                session["user_id"] = user.id
                user_dict = user.to_dict() 
                response = make_response(user_dict, 200)
                return response
        response = make_response({'error': 'unauthorized'}, 401)
        return response



api.add_resource(Login, '/login')

class Signup (Resource):
    def post(self):
        form_json = request.get_json()
        new_user = User (name=form_json ['name'], email=form_json['email'])
        new_user.password_hash = form_json ['password']
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        response = make_response(
            new_user.to_dict(),
            201
        )
        return response

api.add_resource(Signup, '/signup')


class SkiResorts(Resource):
    def get(self):
        resort_list = [resort.to_dict() for resort in Resort.query.all()]
        # resorts = Resort.query.all()
        # resort_list = []
        # for resort in resorts:
        #     resort_dict = {
        #         'id': resort.id,
        #         'name': resort.name,
        #         'location_region': resort.location_region,
        #         'location_state': resort.location_state
        #     }
        #     resort_list.append(resort_dict)
        return make_response(resort_list, 200)

api.add_resource(SkiResorts, '/skiresorts')

class GetCommentsForUser(Resource):
    def get(self, user_id):
        comments = Comment.query.filter_by(user_id=user_id).all()
        return jsonify({'comments': [comment.to_dict() for comment in comments]})

api.add_resource(GetCommentsForUser, '/user-comments/<int:user_id>')


class NewComment(Resource):
    def post(self):
        try:
            data = request.get_json()

            # Query for the resort with the given id
            resort = Resort.query.filter_by(id=data['resort']).first()

            # Retrieve user information from the session cookie
            user_id = session.get('user_id')
            # You can retrieve other user information as needed from the session

            if not user_id:
                return make_response({'error': 'User not authenticated'}, 500)

            # Create the comment with the resort, user, and comment image link
            comment = Comment(comment=data['comment'], user_id=user_id, resort_id=resort.id, comment_image=data['commentImageLink'])
            db.session.add(comment)
            db.session.commit()

            return make_response(comment.to_dict(), 201)
        except Exception as e:
            traceback.print_exc()
            return make_response({'error': str(e)}, 500)





api.add_resource(NewComment, '/comments')

class ModifyComment(Resource):
    def patch(self, comment_id):
        try:
            data = request.get_json()

            # find the comment with the given id
            comment = Comment.query.get(comment_id)

            # update the comment text
            comment.comment = data['comment']

            db.session.commit()

            return make_response(comment.to_dict(), 200)
        except Exception as e:
            traceback.print_exc()
            return make_response({'error': str(e)}, 500)
api.add_resource(ModifyComment, '/changecomment/<int:comment_id>')

class DeleteComment(Resource):
    def delete(self, comment_id):
        try:
            comment = Comment.query.filter_by(id=comment_id).first()
            if comment:
                db.session.delete(comment)
                db.session.commit()
                return make_response({'message': 'Comment deleted successfully'}, 200)
            else:
                return make_response({'error': 'Comment not found'}, 404)
        except Exception as e:
            return make_response({'error': str(e)}, 500)
        
api.add_resource(DeleteComment, '/deletecomment/<int:comment_id>')

class ShowAllComments(Resource):
    def get(self):
        comments = Comment.query.all()
        comments_data = []
        for comment in comments:
            comment_data = {
                'id': comment.id,
                'comment': comment.comment,
                'comment_image': comment.comment_image,
                'user_name': comment.user.name,
                'resort_name': comment.resort.name
            }
            comments_data.append(comment_data)
        return jsonify(comments_data)

api.add_resource(ShowAllComments, '/showcomments')

# Resorts has many users through comments

# class ShowUsersofResort(Resource):
#     def get(self, resort_id):
#         resort = Resort.query.get(resort_id)
#         if resort is None:
#             return jsonify({'error': 'Resort not found'}), 404

#         users = [comment.user.to_dict() for comment in resort.comments if comment.user is not None]
#         return jsonify(users), 200
    
# api.add_resource(ShowUsersofResort, '/resorts/<int:resort_id>/users')

if __name__ == '__main__':
    app.run(port=5555)

