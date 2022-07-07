# 0x03 - Log Parsing

This project is about writing a script that reads `stdin` line by line and computes metrics

 - Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (If the format is not this one the line must be skipped)
 - The algorithm prints the following statistics every 10 lines or upon a keyboard interrupt (`Ctrl + C`), from the beginning:
   - Total file size: `File size: <total size>`, where `,total size>` is the sum of all previous `file size` 
   - Number of lines by status code:
     * Possible status codes `[200, 301, 400, 401, 403, 404, 405, 500]`
     * If a status code doesn't appear or is not an integer, nothing should be printed
     * format `<status code>: <number>`
     * status codes should be printed in ascending order