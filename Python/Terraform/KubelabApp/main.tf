module network-infrastructure{
    net-wordpress1
}

module "ec2" {
    wordpress1
}

// pri potrena na povekje instanci moze samo:

module network-infrastructure{
    net-wordpress2
}

module "ec2" {
    source = "./modles/ec2"
  wordpress2
}
