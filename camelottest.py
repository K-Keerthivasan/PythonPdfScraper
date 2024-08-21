import tabula

# Extract tables from the PDF
tables = tabula.read_pdf("2.ArcBiox™ BGF30–HA - ABMcomposite.pdf", pages='all', multiple_tables=True)

# Print the first table
print(tables[0])
