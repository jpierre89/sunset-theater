def populate(db):
    """Populates database with admin and initial theater data"""

    from flask import current_app
    from app.models.user import User
    from app.models.role import Role

    # Create admin
    admin_role = Role(name='superuser')
    db.session.add(admin_role)
    try:
        db.session.commit()
    except Exception as e:
        print("admin role already exists")
    admin_user = User(
        username=current_app.config["ADMIN_USERNAME"],
        email=current_app.config["ADMIN_EMAIL"],
        password=current_app.config["ADMIN_PASSWORD"],
        roles=[admin_role,],
        active=True
    )
    db.session.add(admin_user)
    try:
        db.session.commit()
    except Exception as e:
        print("admin user already exists")

    # Create theater models
    import datetime

    from app.models.genre import Genre
    from app.models.actor import Actor
    from app.models.director import Director
    from app.models.movie import Movie    
    
    from app.models.auditorium import Auditorium
    from app.models.seat import Seat
    from app.models.show import Show

    # Genres
    action = Genre(name="Action")
    comedy = Genre(name="Comedy")
    drama = Genre(name="Drama")
    db.session.add_all([
        action,
        comedy,
        drama
    ])

    # Actors
    ridley = Actor(name="Daisey Ridley")
    driver = Actor(name="Adam Driver")
    cooper = Actor(name="Bradley Cooper")
    lawrence = Actor(name="Jennifer Lawrence")
    eisenberg = Actor(name="Jesse Eisenberg")
    garfield = Actor(name="Andrew Garfield")
    db.session.add_all([
        ridley,
        driver,
        cooper,
        lawrence,
        eisenberg,
        garfield,
    ])

    # Directors
    johnson = Director(name="Rian Johnson")
    russel = Director(name="David O. Russel")
    fincher = Director(name="David Fincher")
    db.session.add_all([
        johnson,
        russel,
        fincher,
    ])

    # Movies
    last_jedi = Movie(
        title="The Last Jedi",
        genre=action,
        actors=[ridley, driver],
        director=johnson,
        description="The Last Jedi follows Rey as she seeks the aid of Luke Skywalker, "
                   "in hopes of turning the tide for the Resistance in the fight "
                   "against Kylo Ren and the First Order, while General Leia Organa, "
                   "Finn, and Poe Dameron attempt to escape a First Order attack on "
                   "the dwindling Resistance fleet.",
        rating="PG13",
        runtime=datetime.time(2, 30)
    )
    silver_lining = Movie(
        title="Silver Linings Playbook",
        genre=comedy,
        actors=[cooper, lawrence],
        director=russel,
        description="After losing his job and wife, and spending time in a mental institution, "
                    "Pat Solatano (Bradley Cooper) winds up living with his parents "
                    "(Robert De Niro, Jacki Weaver). He wants to rebuild his life and reunite with "
                    "his wife, but his parents would be happy if he just shared their obsession "
                    "with the Philadelphia Eagles. Things get complicated when Pat meets Tiffany "
                    "(Jennifer Lawrence), who offers to help him reconnect with his wife, "
                    "if he will do something very important for her in exchange.",
        rating="PG13",
        runtime=datetime.time(2, 2)
    )
    social_network = Movie(
        title="The Social Network",
        genre=drama,
        actors=[eisenberg, garfield],
        director=fincher,
        description="In 2003, Harvard undergrad and computer genius Mark Zuckerberg (Jesse Eisenberg) "
                    "begins work on a new concept that eventually turns into the global social network "
                    "known as Facebook.",
        rating="PG13",
        runtime=datetime.time(2, 1)
    )
    db.session.add_all([
        last_jedi, silver_lining, social_network
    ])

    # Auditorium
    screen1 = Auditorium(name="Screen 1")
    screen2 = Auditorium(name="Screen 2")
    screen3 = Auditorium(name="Screen 3")
    db.session.add_all([
        screen1, screen2, screen3
    ])

    ######### 
    # Seating
    #########

    # screen1
    for row in ('A', 'B', 'C', 'D', 'E',):
        for i in range(1,13):  #seat number
            db.session.add(
                Seat(
                    number=row + str(i),
                    row=row,
                    auditorium=screen1,
                    is_empty_space= True if i == 7 else False
                )  
            )    
    for i in range(1,13):  # empty row  
        db.session.add(
            Seat(
                number='F' + str(i),
                row=row,
                auditorium=screen1,
                is_empty_space= True
            )  
        )
    for row in ('G', 'H'):    
        for i in range(1,13):
            db.session.add(
                Seat(
                    number=row + str(i),
                    row=row,
                    auditorium=screen1,
                    is_empty_space= False
            )  
        )


    # screen2
    for row in ('A', 'B', 'C', 'D', 'E'):
        for i in range(1,15):  #seat number
            db.session.add(
                Seat(
                    number=row + str(i),
                    row=row,
                    auditorium=screen2,
                    is_empty_space=False
                )  
            )
    for i in range(1,15): # empty row
        db.session.add(
            Seat(
                number='F' + str(i),
                row='F',
                auditorium=screen2,
                is_empty_space = True
            )
        )
    for i in range(1,15):
        db.session.add(
            Seat(
                number='G' + str(i),
                row='G',
                auditorium=screen2,
                is_empty_space = True if i == 1 or i == 2 or i == 13 or i == 14 else False
            )
        )
    for i in range(1,15):
        db.session.add(
            Seat(
                number='H' + str(i),
                row='H',
                auditorium=screen2,
                is_empty_space = True if i == 1 or i == 13 else False
            )
        )
    
    # screen3
    for row in ('A', 'B', 'C', 'D', 'E'):
        for i in range(1,10):  #seat number
            db.session.add(
                Seat(
                    number=row + str(i),
                    row=row,
                    auditorium=screen3,
                    is_empty_space= True if i == 5 else False
                )  
            )

   
    # Shows
    
    # last jedi - screen1
    for movie in (last_jedi,):
        showdate = datetime.date.today()
        for i in range(7):  # next 7 days
            for showtime in ((10, 0), (13, 30), (17, 15), (21, 45)):
                db.session.add(
                    Show(
                        time=datetime.time(*showtime),
                        date=showdate,
                        movie=movie,
                        auditorium=screen1,
                    )
                )     
            showdate = showdate + datetime.timedelta(hours=24)

    # silver lining - screen2
    for movie in (silver_lining,):  
        showdate = datetime.date.today()
        for i in range(7):  # next 7 days
            for showtime in ((9, 0), (12, 15), (16, 0), (22, 30)):
                db.session.add(
                    Show(
                        time=datetime.time(*showtime),
                        date=showdate,
                        movie=movie,
                        auditorium=screen2,
                    )
                )     
            showdate = showdate + datetime.timedelta(hours=24)

    # social network - screen3
    for movie in (social_network,):
        showdate = datetime.date.today()
        for i in range(7):  # next 7 days
            for showtime in ((9, 30), (11, 45), (14, 0), (19, 45)):
                db.session.add(
                    Show(
                        time=datetime.time(*showtime),
                        date=showdate,
                        movie=movie,
                        auditorium=screen3,
                    )
                )     
            showdate = showdate + datetime.timedelta(hours=24)


    try:
        db.session.commit()
    except Exception as e:
        print(f"Models may already exist: {e}")
