"""Lista zakupów"""

zakupy  = {}
zakupy.update({'piekarnia': ['chleb', 'bułki', 'pączek']})
zakupy.update({'warzywniak': ['marchew', 'seler', 'rukola']})

lba_produktów = 0
print("Lista zakupów")
for sklep, produkty in zakupy.items():
    print(f"Idę do {str(sklep).capitalize()} i kupuję tam: {[i.capitalize() for i in produkty]}")
    lba_produktów += len(produkty)
print(f'W sumie kupuję {lba_produktów} produktów')

print("Nie spodziewałem się hiszpańskiej inkwizycji!"
