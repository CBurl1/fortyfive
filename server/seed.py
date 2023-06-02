

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, Resort, User, Comment

with app.app_context():

    print("Deleting data...")

    Resort.query.delete()
    Comment.query.delete()


    print("Creating Resorts...")

    r1 = Resort(name='Sunday River', location_region="USA East", location_state="ME", image = "https://dnyjvzj5aqor7.cloudfront.net/logos/a06da3cf-1263-11e3-b54c-c42c031157e6/zirdPIffaGXZKy1NoURpRUzmwzrVIg00uIkqRR8r.png")
    r2 = Resort(name='Sugarloaf', location_region="USA East", location_state="ME", image = "https://assets.simpleviewinc.com/simpleview/image/fetch/c_limit,q_75,w_1200/https://assets.simpleviewinc.com/simpleview/image/upload/crm/maineta/Sugarloaf-Logo_EC653FF3-5056-A36A-08C56853BB571080-ec653f2f5056a36_ec654067-5056-a36a-086d3b551097d57a.png")
    r3 =  Resort(name='Sugarbush', location_region="USA East", location_state="VT", image = "https://image4.owler.com/logo/sugarbush-resort_owler_20191114_052255_original.png")
    r4 = Resort(name='Killington', location_region="USA East", location_state="VT", image = "https://logovtor.com/wp-content/uploads/2021/11/killington-logo-vector.png")
    r5 = Resort(name='Stratton', location_region="USA East", location_state="VT", image = "https://cdn.shopify.com/s/files/1/0288/8668/products/stratton_sticker@2x.jpg?v=1574956648")
    r6 = Resort(name='Loon', location_region="USA East", location_state="NH", image = "https://upload.wikimedia.org/wikipedia/commons/0/04/Loon_Mountain_Logo.png")
    r7 = Resort(name='Windham', location_region="USA East", location_state="NY", image = "https://www.buyingreene.com/wp-content/uploads/2014/09/win_logo.jpg")
    r8 = Resort(name='Snowshoe', location_region="USA East", location_state="WV", image = "data:image/png;base64,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")


    resorts = [r1, r2, r3, r4, r5, r6, r7, r8]
    print("Creating Comments...")
    c1 = Comment(comment="Great jumps in the terrain park!", user_id=1, resort_id=1)
    c2 = Comment(comment="Perfect weather for hitting the rails!", user_id=2, resort_id=1)
    c3 = Comment(comment="The terrain park at this resort is epic!", user_id=3, resort_id=1)
    c4 = Comment(comment="Loving the variety of features in the park!", user_id=4, resort_id=1)
    c5 = Comment(comment="The jumps here are massive!", user_id=5, resort_id=1)
    c6 = Comment(comment="Awesome rail setup in this terrain park!", user_id=1, resort_id=2)
    c7 = Comment(comment="Had a blast on the boxes today!", user_id=2, resort_id=2)
    c8 = Comment(comment="The terrain park at this resort keeps getting better!", user_id=3, resort_id=2)
    c9 = Comment(comment="Impressed with the creativity of the park features!", user_id=4, resort_id=2)
    c10 = Comment(comment="The jumps are dialed in perfectly!", user_id=5, resort_id=2)
    c11 = Comment(comment="This resort's terrain park is top-notch!", user_id=1, resort_id=3)
    c12 = Comment(comment="The rails here are so smooth!", user_id=2, resort_id=3)
    c13 = Comment(comment="Enjoying the challenges of this park!", user_id=3, resort_id=3)
    c14 = Comment(comment="The jumps provide a great adrenaline rush!", user_id=4, resort_id=3)
    c15 = Comment(comment="The terrain park setup is on point!", user_id=5, resort_id=3)
    c16 = Comment(comment="Had an amazing session in the terrain park today!", user_id=1, resort_id=4)
    c17 = Comment(comment="The rails are perfect for practicing tricks!", user_id=2, resort_id=4)
    c18 = Comment(comment="The variety of features here keeps it interesting!", user_id=3, resort_id=4)
    c19 = Comment(comment="The jumps are sending me to new heights!", user_id=4, resort_id=4)
    c20 = Comment(comment="The terrain park here is a freestyler's dream!", user_id=5, resort_id=4)
    c21 = Comment(comment="The terrain park at this resort is legendary!", user_id=1, resort_id=5)
    c22 = Comment(comment="The rails are so well-maintained!", user_id=2, resort_id=5)
    c23 = Comment(comment="Loving the flow of this park!", user_id=3, resort_id=5)
    c24 = Comment(comment="The jumps here provide an incredible thrill!", user_id=4, resort_id=5)
    c25 = Comment(comment="The terrain park keeps getting better every year!", user_id=5, resort_id=5)
    c26 = Comment(comment="This resort's terrain park is a hidden gem!", user_id=1, resort_id=6)
    c27 = Comment(comment="The rail features are unique and challenging!", user_id=2, resort_id=6)
    c28 = Comment(comment="Had a great time exploring this park!", user_id=3, resort_id=6)
    c29 = Comment(comment="The jumps here have a great launch!", user_id=4, resort_id=6)
    c30 = Comment(comment="The terrain park setup here is impressive!", user_id=5, resort_id=6)
    c31 = Comment(comment="The terrain park at this resort is a must-try!", user_id=1, resort_id=7)
    c32 = Comment(comment="The rail combinations here are mind-blowing!", user_id=2, resort_id=7)
    c33 = Comment(comment="The features in this park are perfect for progression!", user_id=3, resort_id=7)
    c34 = Comment(comment="The jumps offer a great opportunity for airtime!", user_id=4, resort_id=7)
    c35 = Comment(comment="This terrain park is a freestyle paradise!", user_id=5, resort_id=7)
    c36 = Comment(comment="The terrain park at this resort is next level!", user_id=1, resort_id=8)
    c37 = Comment(comment="The rails are challenging and rewarding!", user_id=2, resort_id=8)
    c38 = Comment(comment="Had an amazing day shredding in this park!", user_id=3, resort_id=8)
    c39 = Comment(comment="The jumps here are perfect for pushing limits!", user_id=4, resort_id=8)
    c40 = Comment(comment="The terrain park layout is well thought out!", user_id=5, resort_id=8)
    c41 = Comment(comment="I can't get enough of this resort's terrain park!", user_id=1, resort_id=1)
    c42 = Comment(comment="The rails provide endless possibilities for tricks!", user_id=2, resort_id=1)
    c43 = Comment(comment="Had a fantastic time exploring this park!", user_id=3, resort_id=1)
    c44 = Comment(comment="The jumps here are adrenaline-pumping!", user_id=4, resort_id=1)
    c45 = Comment(comment="The terrain park here is a freestyle heaven!", user_id=5, resort_id=1)
    c46 = Comment(comment="The terrain park at this resort is unbeatable!", user_id=1, resort_id=2)
    c47 = Comment(comment="The rails are so buttery smooth!", user_id=2, resort_id=2)
    c48 = Comment(comment="Loving the flow and creativity of this park!", user_id=3, resort_id=2)
    c49 = Comment(comment="The jumps here are massive!", user_id=4, resort_id=2)
    c50 = Comment(comment="The terrain park setup is simply outstanding!", user_id=5, resort_id=2)
    c51 = Comment(comment = "New C-rail", comment_image = "https://i.pinimg.com/736x/75/2b/8a/752b8a6db93200a80e1c301148e3ffa7--the-photo-lips.jpg", user_id = 1, resort_id = 1)
    c52 = Comment(comment = "Booters were clean this morning", comment_image = "https://www.theirregular.com/wp-content/uploads/images/2018-10-03/34p1.jpg", user_id = 2, resort_id = 2)

    comments = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40, c41, c42, c43, c44, c45, c46, c47, c48, c49, c50, c51, c52]
    
    db.session.add_all(resorts)
    db.session.add_all(comments)
    db.session.commit()
    print("Seeding done!")    


