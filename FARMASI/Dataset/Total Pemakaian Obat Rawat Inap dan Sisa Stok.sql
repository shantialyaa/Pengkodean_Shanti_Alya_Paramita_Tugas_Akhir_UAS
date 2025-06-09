SELECT 
  p.Obat,
  p.Kode_Obat,
  SUM(p.Unit) AS Total_Unit_Digunakan,
  SUM(p.Total_Harga_Pokok) AS Total_Harga_Pokok_Digunakan,
  MAX(p.Unit_Sisa) AS Sisa_Stok
FROM 
  `pharmacy_dataset.pemakaian_obat_rawat_inap_2023` p
GROUP BY 
  p.Obat, p.Kode_Obat
ORDER BY 
  Total_Harga_Pokok_Digunakan DESC;