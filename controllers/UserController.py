from flask import Response, request
from models.User import User, db 
import json

def index():
  session = db.session()
  users = session.query(User).all()
  users_json = [user.serialize() for user in users]
  session.close()
  return Response(json.dumps(users_json))

def store():
  print(request)
  body = request.get_json()
  print(body)
  session = db.session()
  try:
    user = User(name=body['name'],age=body['age'],address=body['address'])
    session.add(user)
    session.commit()
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    session.rollback()
    return {"erro":"não conseguimos gravar o usuário"}
  finally:
    session.close()

def show(user_id):
  session = db.session()
  try:
    user = session.query(User).get(user_id)
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    session.rollback()
    return {"erro":"não conseguimos retornar o usuário"}
  finally:
    session.close()
  
  
def update(user_id):
  session = db.session()
  try:
    body = request.get_json()
    user = session.query(User).get(user_id)

    if body and body['name']:
      user.name = body['name']
    if body and body['age']:
      user.age = body['age']
    if body and body['address']:
      user.address = body['address']

    session.commit()
    return {"ok":"Conseguimos modificar o usuário"}
  except Exception as e:
    session.rollback()
    return {"erro":"não conseguimos atualizar o usuário"}
  finally:
    session.close()

def destroy(user_id):
  session = db.session()
  try:
    user = session.query(User).get(user_id)
    session.delete(user)
    session.commit()
    return {"ok":"Conseguimos deletar o usuário"}
  except Exception as e:
    session.rollback()
    return {"erro":"não conseguimos deletar o usuário"}
  finally:
    session.close()