//this is a file for testing purposes
//TODO: once redux is integrated properly, delete this file.

import store from "./store/index";
import { addArticle } from "./actions/index";

window.store = store;
window.addArticle = addArticle;
