import menu from "./menu.ts";
const source = Deno.readTextFileSync("pdf.txt");
const chapterIndices = [];

for (let i = 0; i < menu.length; i++) {
  const title = menu[i].toUpperCase() + "\n";

  const idx = source.indexOf(title);

  if (idx > -1) {
    console.log("find chapter: ", title);
    chapterIndices.push(idx);
  } else {
    console.log("not find chapter: ", title);
    break;
  }
}

console.log(chapterIndices);

for (let i = 0; i < chapterIndices.length; i++) {
  const title = menu[i];
  const content =
    i === chapterIndices.length - 1
      ? source.slice(chapterIndices[i])
      : source.slice(chapterIndices[i], chapterIndices[i + 1]);

  Deno.writeTextFileSync(`./chapters/${title}.txt`, content);
}
