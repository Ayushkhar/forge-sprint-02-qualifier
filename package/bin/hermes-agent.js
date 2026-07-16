#!/usr/bin/env node

const { runHermes } = require("../lib/python-launcher");

runHermes("hermes-agent", process.argv.slice(2));
