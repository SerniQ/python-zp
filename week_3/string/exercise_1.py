# Dostosuj program liczący wartość lokaty tak aby
# wyświetlał ją z dokładnością do groszy (dwóch liczb po przecinku)


print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value_input = input("Jaką kwotę wpłaciłeś/wpłaciłaś? ")
initial_value = int(initial_value_input)
percentage_input = input("Jakie jest oprocentowanie (%)? ")
percentage = int(percentage_input)
years_input = input("Ile lat trwa lokata? ")
years = int(years_input)

final_value = initial_value * (1 + percentage / 100) ** years

print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

