ikoodid=[]
arvud=[]

haiglad = {
    range(001, 011): "Kuressaare Haigla",
    range(011, 020): "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu",
    range(021, 221): "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla",
    range(221, 271): "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)",
    range(271, 371): "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla",
    range(371, 421): "Narva Haigla",
    range(421, 471): "Pärnu Haigla",
    range(471, 491): "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla",
    range(491, 521): "Järvamaa Haigla (Paide)",
    range(521, 571): "Rakvere, Tapa haigla",
    range(571, 601): "Valga Haigla",
    range(601, 651): "Viljandi Haigla",
    range(651, 701): "Lõuna-Eesti Haigla (Võru), Põlva Haigla"}

def kontrollnumber(code):
    astme_kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    astme_kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]



