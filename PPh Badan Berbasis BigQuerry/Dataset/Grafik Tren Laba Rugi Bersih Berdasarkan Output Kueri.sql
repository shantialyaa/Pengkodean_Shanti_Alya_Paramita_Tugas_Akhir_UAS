SELECT
  tahun,
  pendapatan,
  beban_operasional,
  penyusutan,
  skenario,
  (pendapatan - (beban_operasional + penyusutan)) AS laba_kotor
FROM `PPh_Badan_Berbasis_BigQuerry.transaksi_keuangan`
ORDER BY tahun, skenario;