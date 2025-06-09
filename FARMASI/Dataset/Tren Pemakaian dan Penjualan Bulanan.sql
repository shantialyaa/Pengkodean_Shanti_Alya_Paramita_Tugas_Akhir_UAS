WITH PemakaianBulanan AS (
  SELECT 
    EXTRACT(MONTH FROM Tanggal_Pemakaian) AS Bulan,
    Obat,
    Kode_Obat,
    SUM(Unit) AS Total_Unit_Pemakaian
  FROM 
    `pharmacy_dataset.pemakaian_obat_rawat_inap_2023`
  GROUP BY 
    EXTRACT(MONTH FROM Tanggal_Pemakaian), Obat, Kode_Obat
),
PenjualanBulanan AS (
  SELECT 
    EXTRACT(MONTH FROM Tanggal_Penjualan) AS Bulan,
    Obat,
    Kode_Obat,
    SUM(Unit) AS Total_Unit_Penjualan
  FROM 
    `pharmacy_dataset.penjualan_obat_rawat_jalan_2023`
  GROUP BY 
    EXTRACT(MONTH FROM Tanggal_Penjualan), Obat, Kode_Obat
)
SELECT 
  COALESCE(p.Bulan, j.Bulan) AS Bulan,
  COALESCE(p.Obat, j.Obat) AS Obat,
  COALESCE(p.Kode_Obat, j.Kode_Obat) AS Kode_Obat,
  COALESCE(p.Total_Unit_Pemakaian, 0) AS Total_Unit_Pemakaian,
  COALESCE(j.Total_Unit_Penjualan, 0) AS Total_Unit_Penjualan
FROM 
  PemakaianBulanan p
FULL OUTER JOIN 
  PenjualanBulanan j
ON 
  p.Bulan = j.Bulan AND p.Kode_Obat = j.Kode_Obat
ORDER BY 
  Bulan, Obat;