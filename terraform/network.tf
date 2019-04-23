resource "google_compute_network" "vpc_network" {
  name                    = "pyg-dmz-network"
  auto_create_subnetworks = "true"
}

resource "google_compute_firewall" "allow_ssh" {
  name    = "allow-ssh"
  network = "${google_compute_network.vpc_network.name}"

  allow {
    protocol = "tcp"
  }

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }
}
