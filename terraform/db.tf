resource "google_sql_database_instance" "master" {
  name = "pyg-master"
  database_version = "POSTGRES_9_6"

  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_database" "users" {
  name      = "users"
  instance  = "${google_sql_database_instance.master.name}"
  charset   = "UTF8"
  collation = "en_US.UTF8"
}
