import express from "express";

import { initDependencies } from "./dependencies/index.js";

const app = express();

app.use(express.json());

const dependencies = initDependencies();

export default app;
