sites = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
nomes = [site[4: -4] for site in sites]

print(f"{nomes}")