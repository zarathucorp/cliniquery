library(DBI);library(RSQLite);library(dbplyr);library(dplyr)

## Connect
con <- dbConnect(SQLite(), dbname = "cliniquery.db")

## DB list
dbListTables(con)

## Question DB
res<- dbGetQuery(con, "SELECT * FROM questions")
write.csv(res, "questions.csv", row.names = F)



