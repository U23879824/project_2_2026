#PART 2: ABC Classification
#This model groups the SKUs into A, B and C categories based on their usage value in the inventory. 

#Representation of SKU data
skus = [{"sku": "BRK-100", "demand": 2000, "cost": 45},{"sku": "GSK-220", "demand": 1500, "cost": 30},
        {"sku": "BLT-010", "demand": 10000, "cost": 2},{"sku": "BRG-330", "demand": 800, "cost": 60},
        {"sku": "SEAL-500","demand": 3000, "cost": 5},{"sku": "MTR-700", "demand": 50, "cost": 800},
        {"sku": "WSH-050", "demand": 20000, "cost": 0.5},{"sku": "CBL-900", "demand": 400, "cost": 25},
        {"sku": "NUT-200", "demand": 5000, "cost": 1},{"sku": "PIN-300", "demand": 1000, "cost": 10}]

#Calculating usage value per SKU
def usage_value(demand, cost):
   return demand * cost

for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

#Sort descending by value
skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

#Calculate cumulative percentage
total_value = sum(item["value"] for item in skus_sorted)

running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100

#Assigning a tier
def assign_tier(cum_pct):  
    if cum_pct <= 70:
        return "A"
    elif cum_pct <= 90:
        return "B"
    else:
        return "C"

for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])      

#Print the classification report
for item in skus_sorted:
    print(item["sku"], "| value:", item["value"],
          "| cum %:", round(item["cum_pct"], 1),
          "| tier:", item["tier"])

#Count SKUs per tier    
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1
print(tier_counts)    

#5.1. It doesn't change much. The original split was {'A': 3, 'B': 3, 'C': 2}, while the new split is {'A': 4, 'B': 4, 'C': 2}. 
#5.2. Tier A decreases by 1, tier B decreases by 1 and tuer C increases by 2.
#5.3. 
def classify_inventory(skus):

    for item in skus:
        item["value"] = item["demand"] * item["cost"]
    skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)    

    total_value = sum(item["value"] for item in skus_sorted)
    running_total = 0

    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100

        if item["cum_pct"] <= 70:
            item["tier"] = "A"
        elif item["cum_pct"] <= 90:
            item["tier"] = "B"
        else:
            item["tier"] = "C"
    return skus_sorted
    
    

                

