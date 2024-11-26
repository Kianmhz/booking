const fs = require('fs');
const PDFDocument = require('pdfkit');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

const exportToPDF = (data, fileName) => {
    const doc = new PDFDocument();
    doc.pipe(fs.createWriteStream(fileName));
    doc.text(JSON.stringify(data, null, 2));
    doc.end();
};

const exportToCSV = async (data, fileName) => {
    const csvWriter = createCsvWriter({
        path: fileName,
        header: Object.keys(data[0]).map((key) => ({ id: key, title: key })),
    });
    await csvWriter.writeRecords(data);
};

module.exports = { exportToPDF, exportToCSV };
