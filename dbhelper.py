import pymysql



class DB:
    def __init__(self):
        #connect to the database
        try:
            self.connection = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="Insha@12",
                database="flights"
            )

            self.cursor = self.connection.cursor()
            print("Connected to MySQL successfully")

        except Exception as e:
            print("Connection error:", e)

    def fetch_city_names(self):
        self.cursor.execute("""
                            select distinct(source_city)
                            from flight
                            union
                            select distinct(destination_city)
                            from flight
                            """)

        data = self.cursor.fetchall()
        city = [item[0] for item in data]

        print("Cities:", city)

        return city

    def fetch_all_flights(self, source_city, destination_city):
        self.cursor.execute(""" SELECT airline,flight,departure_time,duration,arrival_time,price
                               FROM flight
                               WHERE source_city = '{}'
                               AND destination_city = '{}' """.format(source_city, destination_city))
        data = self.cursor.fetchall()

        return data

    def fetch_airline_frequency(self):
        airline = []
        frequency = []


        self.cursor.execute("""select airline, count(*) from flight
                                group by airline
                            """)

        data = self.cursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):
        city =[]
        frequency = []
        self.cursor.execute(""" select source_city, count(*) from (select source_city from flight
                              union all
							select destination_city from flight)t
                             group by t.source_city
                              order by count(*) desc
                             """)
        data = self.cursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city, frequency

