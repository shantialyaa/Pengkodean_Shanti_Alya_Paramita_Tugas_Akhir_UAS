SELECT
  t.tahun,
  k.tax_rate,
  k.tax_holiday_awal,
  k.tax_holiday_akhir,
  (t.pendapatan - (t.beban_operasional + t.penyusutan)) AS laba_kena_pajak,
  CASE 
    WHEN t.tahun BETWEEN k.tax_holiday_awal AND k.tax_holiday_akhir THEN 0
    ELSE (t.pendapatan - (t.beban_operasional + t.penyusutan)) * k.tax_rate
  END AS pph_badan
FROM `PPh_Badan_Berbasis_BigQuerry.transaksi_keuangan` t
JOIN `PPh_Badan_Berbasis_BigQuerry.kebijakan_fiskal` k
ON t.tahun = k.tahun
WHERE t.skenario = 'tax_holiday'
ORDER BY t.tahun;