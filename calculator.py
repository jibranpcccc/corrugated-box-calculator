#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrugated Box Blank Area & Volumetric Weight Calculator
Developed by Barkat Packaging (Hyderabad, Sindh, Pakistan)
Official web tool: https://barkatcartons.com/calculator.html
"""

def calculate_box_blank_dimensions(length_in, width_in, height_in, joint_allowance_in=1.5, trim_allowance_in=1.0):
    """
    Calculates the required sheet blank size for a standard Regular Slotted Carton (RSC / FEFCO 0201).
    Formula:
      Blank Length = 2 * (Length + Width) + Joint Allowance
      Blank Width = Width + Height + Trim Allowance
    """
    blank_length = 2 * (length_in + width_in) + joint_allowance_in
    blank_width = width_in + height_in + trim_allowance_in
    blank_area_sq_inches = blank_length * blank_width
    blank_area_sq_ft = blank_area_sq_inches / 144.0
    
    return {
        "blank_length_inches": round(blank_length, 2),
        "blank_width_inches": round(blank_width, 2),
        "blank_area_sq_ft": round(blank_area_sq_ft, 3)
    }

def calculate_volumetric_weight(length_cm, width_cm, height_cm, divisor=5000):
    """
    Standard IATA volumetric weight formula for air freight & courier parcel dispatch.
    """
    return round((length_cm * width_cm * height_cm) / divisor, 2)

if __name__ == "__main__":
    print("==================================================")
    print(" Barkat Packaging - Corrugated Box Calculator Engine ")
    print(" Live 3D Web Calculator: https://barkatcartons.com/calculator.html")
    print("==================================================")
    
    # Example: 18 x 12 x 10 inch 5-ply shipping carton
    L, W, H = 18, 12, 10
    blank = calculate_box_blank_dimensions(L, W, H)
    print(f"\nBox Dimensions: {L}\" x {W}\" x {H}\"")
    print(f"Sheet Blank Length: {blank['blank_length_inches']} inches")
    print(f"Sheet Blank Width:  {blank['blank_width_inches']} inches")
    print(f"Total Sheet Area:   {blank['blank_area_sq_ft']} sq. ft.")
    
    vol_kg = calculate_volumetric_weight(L * 2.54, W * 2.54, H * 2.54)
    print(f"Air Freight Volumetric Weight: {vol_kg} kg")
    print("\nFor custom wholesale quotes and plant manufacturing:")
    print("Visit: https://barkatcartons.com/products.html")
