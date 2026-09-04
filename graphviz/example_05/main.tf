resource "local_file" "bonanza_file" {
    content   = "Bonanza!"
    filename = "${path.module}/bonanza.txt"
}

resource "archive_file" "bonanza_zip" {
    type        = "zip"
    source_file = "${path.module}/bonanza.txt"
    output_path = "${path.module}/bonanza.zip"

   depends_on   = [local_file.bonanza_file]
}
