
# game record clean up functions

# files come with two header lines, combine them
def _merge_headers(input_fn, output_fn):
	with open(input_fn, "r") as f, open(output_fn, "w") as g:
		header1 = f.readline().strip().split(",")
		header2 = f.readline().strip().split(",")

		g.write(",".join([" ".join(filter(None, [h1, h2])) for h1, h2 in zip(header1, header2)]))
		g.write("\n")

		for line in f.readlines():
			g.write(line)

def merge_headers():
	_merge_headers("resources/raw/playoffs.csv", "resources/parsed/playoffs.csv")
	_merge_headers("resources/raw/regular_season.csv", "resources/parsed/regular_season.csv")
	
	for year in range(1989, 2001):
		_merge_headers(f"resources/raw/{year}-team.csv", f"resources/parsed/{year}-team.csv")
		_merge_headers(f"resources/raw/{year}-opp.csv", f"resources/parsed/{year}-opp.csv")

# merge records of separate years into one file
def merge_years(team):
	output_fn = f"resources/parsed/{team}.csv"
	first = True
	with open(output_fn, "w") as g:
		for year in range(1989, 2001):
			input_fn = f"resources/parsed/{year}-{team}.csv"
			with open(input_fn, "r") as f:
				header = f.readline()
				if first:
					g.write(f"year,{header}")
					first = False

				for line in f.readlines():
					g.write(f"{year},{line}")


merge_headers()
merge_years("opp")
merge_years("team")
