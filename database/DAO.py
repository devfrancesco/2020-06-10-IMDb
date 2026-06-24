from database.DB_connect import DBConnect
from model.Attore import Attore
from model.arco import Arco


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllGeneri():
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct mg.genre 
                    from movies_genres mg 
                    order by mg.genre """
        cursor.execute(query)
        for row in cursor:
            results.append(row["genre"])
        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllAttori(genere):
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """select a.*
                    from actors a , roles r , movies_genres mg 
                    where a.id = r.actor_id 
                    and r.movie_id = mg.movie_id 
                    and mg.genre = %s 
                    order by a.last_name"""
        cursor.execute(query, (genere,))
        for row in cursor:
            results.append(Attore(**row))
        cursor.close()
        conn.close()
        return results

    def getAllEdges(genere, idMapA):
        conn = DBConnect.get_connection()
        results = []
        cursor = conn.cursor(dictionary=True)
        query = """ with attori_film as (
                    select a.id as id, r.movie_id as movie,count(*) as comparse
                    from actors a 
                    join roles r on r.actor_id = a.id 
                    join movies_genres mg on mg.movie_id = r.movie_id 
                    where mg.genre = %s
                    group by a.id, r.movie_id 
                    )
                select  af.id as id1, af2.id as id2, SUM(af.comparse + af2.comparse) as peso
                from attori_film af
                join attori_film af2 on af.movie = af2.movie 
                where af.id < af2.id 
                group by af.id, af2.id"""
        cursor.execute(query, (genere,))
        for row in cursor:
            results.append(Arco(idMapA[row['id1']], idMapA[row['id2']], row['peso']))
        cursor.close()
        conn.close()
        return results