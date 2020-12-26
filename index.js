function stopmining() {
            var blob = new Blob(['stop'],
                { type: "text/plain;charset=utf-8" });
            saveAs(blob, "static.txt");
        }