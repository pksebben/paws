resource "google_compute_project_metadata_item" "oslogin" {
  project = "paws-your-game-main"
  key     = "enable-oslogin"
  value   = "TRUE"
}

resource "google_project_iam_binding" "role-binding" {
  project = "paws-your-game-main"
  role    = "roles/compute.osAdminLogin"

  members = [
    "user:ian@pawsyourgame.org",
    "user:ben@pawsyourgame.org"
  ]
}
