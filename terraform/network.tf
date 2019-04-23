resource "google_compute_network" "vpc_network" {
  name                    = "pyg-dmz-network"
  auto_create_subnetworks = "true"
}