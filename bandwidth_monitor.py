import psutil
from rumps import App, timer


class BandwidthMonitor(App):
    def __init__(self):
        super().__init__("Bandwidth Monitor")
        self.prev_upload, self.prev_download = 0, 0

    @staticmethod
    def format_speed(speed):
        units = ["KB/s", "MB/s", "GB/s", "TB/s"]
        for unit in units:
            if speed > 1024:
                speed /= 1024
                continue
            return f"{speed:.1f} {unit}"

    @timer(1)
    def update_bandwidth(self, _):
        net_io = psutil.net_io_counters()
        upload, download = net_io.bytes_sent, net_io.bytes_recv
        upload_speed, download_speed = (
            (upload - self.prev_upload) / 1024,
            (download - self.prev_download) / 1024,
        )
        self.prev_upload, self.prev_download = upload, download
        self.title = f"{BandwidthMonitor.format_speed(download_speed)} ↓ {BandwidthMonitor.format_speed(upload_speed)} ↑"


if __name__ == "__main__":
    BandwidthMonitor().run()
