"""Builds index.html (one self-contained file) from src/index.template.html + lib/qrcode.min.js."""
import pathlib
root = pathlib.Path(__file__).parent
tpl = (root / "src" / "index.template.html").read_text()
lib = (root / "lib" / "qrcode.min.js").read_text()
assert "</script" not in lib
(root / "index.html").write_text(tpl.replace("<!--QR_LIB-->", "<script>\n" + lib + "\n</script>"))
print("built index.html", (root / "index.html").stat().st_size, "bytes")
