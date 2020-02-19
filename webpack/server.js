const express = require("express")
const app = express()
const port = 3123
app.use("/static/bundles", express.static("bundles"))
app.listen(port, () => console.log(`Wepack server listening on port ${port}!`))
