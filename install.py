import pymysql


db = pymysql.connect("localhost","guest", "1234","numbers" )
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS `numbers`;")
cursor.execute("use numbers")
cursor.execute("CREATE TABLE IF NOT EXISTS `blocklist` (`number` varchar(20) NOT NULL PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS `blacklist` (`number` varchar(20) NOT NULL PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS `whitelist` (`number` varchar(20) NOT NULL PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS `toggle` (`toggle` varchar(20))")
db.commit()
db.close()
