#! /usr/bin/env python

from multiprocessing import Pool
import tqdm
import sys


def main(): 
    if (len(sys.argv)!=2): 
        print(f"Usage: {sys.argv[0]} <filename>")
        exit(0)
    part1(sys.argv[1])
    part2(sys.argv[1])

def part1(filename):
    seed_soil = []
    soil_fert = []
    fert_watr = []
    watr_lght = []
    lght_temp = []
    temp_humi = []
    humi_loca = []
    lowest_loca = None
    seeds=[]
    with open(filename, "r") as f:
        while ( line := f.readline() ):
            line = line.strip()
            if line.startswith("seeds:"): 
                seeds = [int(seed) for seed in line.split()[1:]]
            if "seed-to-soil" in line: 
                while( line := f.readline().strip() ):
                   seed_soil.append([int(num) for num in line.split()])
            if "soil-to-fertilizer" in line: 
                while( line := f.readline().strip() ):
                   soil_fert.append([int(num) for num in line.split()])
            if "fertilizer-to-water" in line: 
                while( line := f.readline().strip() ):
                   fert_watr.append([int(num) for num in line.split()])
            if "water-to-light" in line: 
                while( line := f.readline().strip() ):
                   watr_lght.append([int(num) for num in line.split()])
            if "light-to-temperature" in line: 
                while( line := f.readline().strip() ):
                   lght_temp.append([int(num) for num in line.split()])
            if "temperature-to-humidity" in line: 
                while( line := f.readline().strip() ):
                   temp_humi.append([int(num) for num in line.split()])
            if "humidity-to-location" in line: 
                while( line := f.readline().strip() ):
                   humi_loca.append([int(num) for num in line.split()])

    for seed in seeds: 
        soil = translate(seed, seed_soil)
        fert = translate(soil, soil_fert)
        watr = translate(fert, fert_watr)
        lght = translate(watr, watr_lght)
        temp = translate(lght, lght_temp)
        humi = translate(temp, temp_humi)
        loca = translate(humi, humi_loca)
        lowest_loca = loca if not lowest_loca else loca if lowest_loca>loca else lowest_loca

    print("Part 1: ", lowest_loca)

def part2(filename):
    seed_soil = []
    soil_fert = []
    fert_watr = []
    watr_lght = []
    lght_temp = []
    temp_humi = []
    humi_loca = []
    lowest_loca = None
    seeds=[]
    ranges=[]
    with open(filename, "r") as f:
        while ( line := f.readline() ):
            line = line.strip()
            if line.startswith("seeds:"): 
                seedranges = [int(seed) for seed in line.split()[1:]]
                ranges = [*zip(seedranges[::2], seedranges[1::2])]
            if "seed-to-soil" in line: 
                while( line := f.readline().strip() ):
                   seed_soil.append([int(num) for num in line.split()])
            if "soil-to-fertilizer" in line: 
                while( line := f.readline().strip() ):
                   soil_fert.append([int(num) for num in line.split()])
            if "fertilizer-to-water" in line: 
                while( line := f.readline().strip() ):
                   fert_watr.append([int(num) for num in line.split()])
            if "water-to-light" in line: 
                while( line := f.readline().strip() ):
                   watr_lght.append([int(num) for num in line.split()])
            if "light-to-temperature" in line: 
                while( line := f.readline().strip() ):
                   lght_temp.append([int(num) for num in line.split()])
            if "temperature-to-humidity" in line: 
                while( line := f.readline().strip() ):
                   temp_humi.append([int(num) for num in line.split()])
            if "humidity-to-location" in line: 
                while( line := f.readline().strip() ):
                   humi_loca.append([int(num) for num in line.split()])


    loca = 1
    while (True):
       humi = backtranslate(loca, humi_loca) 
       temp = backtranslate(humi, temp_humi) 
       lght = backtranslate(temp, lght_temp) 
       watr = backtranslate(lght, watr_lght) 
       fert = backtranslate(watr, fert_watr) 
       soil = backtranslate(fert, soil_fert) 
       seed = backtranslate(soil, seed_soil) 
       for rng in ranges:
           if rng[0] <= seed < rng[0] + rng[1]: 
               print("Part 2: ", loca)
               return
       loca += 1



def backtranslate(num, ttable: list):
    retval = [num - (tmap[0] - tmap[1]) for tmap in ttable if tmap[0] <= num < tmap[0]+tmap[2]]
    if len(retval)>1:
        print("Error!!!")
        exit(1)
    retval = retval[0] if retval else num
    return retval
        
def translate(num, ttable: list): 
    retval = [num + (tmap[0] - tmap[1]) for tmap in ttable if tmap[1] <= num < tmap[1]+tmap[2]] 
    if len(retval)>1:
        print("Error!!!")
        exit(1)
    retval = retval[0] if retval else num
    return retval


if __name__ == '__main__':
    main()
