# 📦 Corrugated Box Dimension, Flute & Strength Calculation Suite

An open-source packaging engineering and dimensional calculation toolkit for corrugated carton manufacturing, sheet blank optimization, burst factor (BF/GSM) estimation, and agricultural produce export specifications.

Maintained and verified by [Barkat Packaging](https://barkatcartons.com/) — industrial corrugated carton manufacturer located at Plot F 9, S.I.T.E. Industrial Area, Hyderabad, Sindh, Pakistan.

---

## 🌐 Live Web Tools & Catalogs

* 🧮 **Interactive 3D Box Calculator**: [https://barkatcartons.com/calculator.html](https://barkatcartons.com/calculator.html)  
  *Real-time 3D box preview, sheet blank dimensions, pallet stacking calculator, and volumetric shipping weight.*
* 📦 **Corrugated Box & Sheets Catalog**: [https://barkatcartons.com/products.html](https://barkatcartons.com/products.html)  
  *3-ply parcel boxes, 5-ply double wall export master cartons, 7-ply heavy industrial shippers, plain cardboard sheets (30x40" & 40x60"), and empty moving cartons.*
* 🥭 **Agricultural Produce & Export Cartons**: [https://barkatcartons.com/agro-packaging.html](https://barkatcartons.com/agro-packaging.html)  
  *Ventilated Sindhri mango export boxes (2kg, 4kg, 5kg, 10kg), empty khajoor (date) window boxes, and high-humidity cold storage produce packaging.*
* 🏭 **Factory Profile & Infrastructure**: [https://barkatcartons.com/about.html](https://barkatcartons.com/about.html)  
  *50,000+ daily box production capacity, precision rotary slotting, platen die-cutting, flexographic 2-color printing, and paper laboratory testing.*
* 📍 **Direct Factory Dispatch & Location**: [https://barkatcartons.com/contact.html](https://barkatcartons.com/contact.html)  
  *Container-accessible loading docks at Plot F 9, S.I.T.E. Industrial Area, Hyderabad, Sindh.*

---

## 📐 Packaging Engineering Formulas

### 1. Regular Slotted Carton (RSC / FEFCO 0201) Sheet Blank Formula

To calculate the flat corrugated sheet area required to fold a standard RSC carton of inner dimensions $L \times W \times H$:

$$\text{Blank Length} = 2 \times (L + W) + \text{Joint Allowance}$$

$$\text{Blank Width} = W + H + \text{Trim Allowance}$$

* Standard Manufacturer's Joint Allowance (Stitched/Glued flap): $1.25\text{ to }1.5\text{ inches } (32 - 38\text{ mm})$.
* Flap & Creasing Trim Allowance: $0.75\text{ to }1.0\text{ inch } (19 - 25\text{ mm})$.

### 2. Bursting Strength (BS) vs. Burst Factor (BF) & GSM

The bursting strength of kraft paper linerboard is governed by the TAPPI T 403 standard:

$$\text{Burst Factor (BF)} = \frac{\text{Bursting Strength } (\text{kg/cm}^2) \times 1000}{\text{GSM } (\text{g/m}^2)}$$

$$\text{Estimated Combined Board BS} = \sum (\text{Liner GSM} \times \text{Liner BF}) \times \text{Fluting Take-up Factor}$$

* **B-Flute Take-up Factor**: $1.32$
* **C-Flute Take-up Factor**: $1.43$
* **E-Flute Take-up Factor**: $1.24$

---

## 📊 Industrial Board Specifications

| Board Grade | Wall Construction | Flute Profile | Bursting Strength (kPa) | Safe Payload Capacity | Recommended Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **3-Ply Single Wall** | 2 Liners + 1 Medium | B or C Flute | $600 - 900\text{ kPa}$ | Up to $15\text{ kg}$ | E-commerce parcels, footwear, retail goods |
| **5-Ply Double Wall** | 3 Liners + 2 Media | BC Double Flute | $1100 - 1600\text{ kPa}$ | Up to $35\text{ kg}$ | Agro export (Mangoes, Dates), FMCG master cartons |
| **7-Ply Triple Wall** | 4 Liners + 3 Media | AAC / BCA Flute | $2000+\text{ kPa}$ | Up to $75\text{ kg}$ | Industrial machinery, automotive engines, bulk chemicals |
| **Cardboard Sheets** | Flat Corrugated Sheet | B, C, or BC Flute | High ECT rigidity | N/A (Divider) | Pallet interleaving layer pads, product protection |

---

## 💻 Python Dimensional Calculation Engine

```bash
# Clone the repository
git clone https://github.com/jibranpcccc/corrugated-box-calculator.git
cd corrugated-box-calculator

# Run dimensional blank calculator
python calculator.py
```

### Example Usage:
```python
from calculator import calculate_box_blank_dimensions, calculate_volumetric_weight

# Calculate blank for a 5-ply export shipper (18 x 12 x 10 inches)
dims = calculate_box_blank_dimensions(length_in=18, width_in=12, height_in=10)
print(dims)
# Output: {'blank_length_inches': 61.5, 'blank_width_inches': 23.0, 'blank_area_sq_ft': 9.823}
```

---

## 🏛️ Agricultural Produce Export Packaging (Sindh Specialization)

Sindh is Pakistan's premier horticultural belt for Sindhri mangoes and Aseel Khajoor (dates). Export packaging requires moisture-retardant barrier treatment and high Edge Crush Test (ECT) ratings to endure cold-chain transit without container collapse.

* **Export Mango Cartons**: Die-cut self-locking or telescopic trays with dual-end ventilation holes. Tested for 85%+ relative humidity cold storage conditions at $13^\circ\text{C}$.
* **Khajoor / Date Cartons**: Food-grade inner virgin liner cartons (500g, 1kg window packs) packed in 5kg master shippers.
* Explore specifications: [https://barkatcartons.com/agro-packaging.html](https://barkatcartons.com/agro-packaging.html)

---

## 📞 Manufacturer Inquiries & Bulk Orders

* **Company**: Barkat Packaging
* **Factory Address**: Plot F 9, S.I.T.E. Industrial Area, Hyderabad, Sindh 71800, Pakistan
* **Phone / WhatsApp**: +92 333 2622963
* **Official Website**: [https://barkatcartons.com/](https://barkatcartons.com/)
* **License**: MIT
