#PART 1: Economic Production Quantity (EPQ)
#This model calculates the optimal production quantity for a product based on its demand, setup cost, holding cost, and production rate.
import math

#Define inputs
annual_demand = 12000         #units per year
setup_cost = 50               #cost per production run (in Rands)
holding_cost = 2              #cost per unit per year (in Rands)   
daily_demand_rate = 40        #units produced or sold per day
daily_production_rate = 100000   #units the process can make per day

#EPQ function
def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
 return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))
epq = calculate_epq(annual_demand, setup_cost, holding_cost, daily_demand_rate, daily_production_rate)
print("Optimal production quantity:", round(epq, 2))

#Calculate production runs/year & run length
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))

#Calculate maximum inventory level
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)
print("Maximum inventory level:", round(max_inventory, 2))

#5.1. The EPQ goes down. This makes sense because the higher production rate allows products to be produced faster, so a smaller batch is produced.
# This helps reduce the amount of inventory held and therefore reduces holding costs. 

#5.2. The EOQ is 774.59 and the EPQ is 774.75. The values are almost the same, with a difference of 0.16 units. 
# The values are very similar because the production rate is much higher than the demand rate.