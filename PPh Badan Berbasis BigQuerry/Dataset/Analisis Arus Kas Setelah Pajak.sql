SELECT
  t.tahun,
  t.skenario,
  (t.pendapatan - (t.beban_operasional + t.penyusutan)) AS laba_kena_pajak,
  CASE 
    WHEN t.skenario = 'tax_holiday' AND t.tahun BETWEEN k.tax_holiday_awal AND k.tax_holiday_akhir THEN 0
    ELSE (t.pendapatan - (t.beban_operasional + t.penyusutan)) * k.tax_rate
  END AS pph_badan,
  (t.pendapatan - (t.beban_operasional + t.penyusutan)) - 
  (CASE 
    WHEN t.skenario = 'tax_holiday' AND t.tahun BETWEEN k.tax_holiday_awal AND k.tax_holiday_akhir THEN 0
    ELSE (t.pendapatan - (t.beban_operasional + t.penyusutan)) * k.tax_rate
  END) AS arus_kas_setelah_pajak
FROM `PPh_Badan_Berbasis_BigQuerry.transaksi_keuangan` t
JOIN `PPh_Badan_Berbasis_BigQuerry.kebijakan_fiskal` k
ON t.tahun = k.tahun
ORDER BY t.tahun, t.skenario;