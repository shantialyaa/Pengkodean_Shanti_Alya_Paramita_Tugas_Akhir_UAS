WITH StokAwal AS (
  SELECT 
    Obat,
    Kode_Obat,
    SUM(Unit) AS Stok_Awal,
    SUM(Total_Harga_Pokok) AS Total_Harga_Pokok_Awal
  FROM 
    `pharmacy_dataset.persediaan_farmasi_2023`
  GROUP BY 
    Obat, Kode_Obat
),
Pemakaian AS (
  SELECT 
    Obat,
    Kode_Obat,
    SUM(Unit) AS Total_Pemakaian
  FROM 
    `pharmacy_dataset.pemakaian_obat_rawat_inap_2023`
  GROUP BY 
    Obat, Kode_Obat
),
Penjualan AS (
  SELECT 
    Obat,
    Kode_Obat,
    SUM(Unit) AS Total_Penjualan
  FROM 
    `pharmacy_dataset.penjualan_obat_rawat_jalan_2023`
  GROUP BY 
    Obat, Kode_Obat
)
SELECT 
  s.Obat,
  s.Kode_Obat,
  s.Stok_Awal,
  COALESCE(p.Total_Pemakaian, 0) AS Total_Pemakaian,
  COALESCE(j.Total_Penjualan, 0) AS Total_Penjualan,
  (s.Stok_Awal - COALESCE(p.Total_Pemakaian, 0) - COALESCE(j.Total_Penjualan, 0)) AS Stok_Akhir,
  s.Total_Harga_Pokok_Awal AS Total_Harga_Pokok_Awal
FROM 
  StokAwal s
LEFT JOIN 
  Pemakaian p ON s.Kode_Obat = p.Kode_Obat
LEFT JOIN 
  Penjualan j ON s.Kode_Obat = j.Kode_Obat
ORDER BY 
  Stok_Akhir DESC;