import app from "./app.js";
import { config } from "./config/index.js";

app.listen(config.port, () => {
  console.log(`API Host listening on port ${config.port}`);
});
