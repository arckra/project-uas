#class Data
class Vehicle:
    def __init__(self, jenis, nama, kapasitas):
        self.jenis = jenis
        self.nama = nama
        self.kapasitas = kapasitas

#Class View
class View:
    @staticmethod
    def display_vehicles(vehicles):
        print(f"{'Jenis':<10} {'Nama':<20} {'Kapasitas (L)':<15}")
        print("=" * 45)
        for vehicle in vehicles:
            print(f"{vehicle.jenis:<10} {vehicle.nama:<20} {vehicle.kapasitas:<15}")

#Class Process
class Process:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        try:
            jenis = input("Masukkan jenis kendaraan (motor/mobil): ").strip().lower()
            if jenis not in ['motor', 'mobil']:
                raise ValueError("Jenis kendaraan tidak valid. Harus 'motor' atau 'mobil'.")

            nama = input("Masukkan nama kendaraan: ").strip()
            kapasitas = float(input("Masukkan kapasitas bensin (dalam liter): "))
            if kapasitas <= 0:
                raise ValueError("Kapasitas harus lebih besar dari 0.")

            vehicle = Vehicle(jenis, nama, kapasitas)
            self.vehicles.append(vehicle)
            print("Kendaraan berhasil ditambahkan.")
        except ValueError as e:
            print(f"Error: {e}")

    def show_vehicles(self):
        if not self.vehicles:
            print("Tidak ada kendaraan yang terdaftar.")
        else:
            View.display_vehicles(self.vehicles)

#Main Fungsi
def main():
    process = Process()
    while True:
        print("\nMenu:")
        print("1. Tambah kendaraan")
        print("2. Tampilkan daftar kendaraan")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            process.add_vehicle()
        elif choice == '2':
            process.show_vehicles()
        elif choice == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
