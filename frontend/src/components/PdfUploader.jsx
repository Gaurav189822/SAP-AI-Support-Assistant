import { useState } from "react";
import axios from "axios";
import { FiUploadCloud } from "react-icons/fi";

export default function PdfUploader() {

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleUpload = async () => {

    if (!file) return;

    const formData = new FormData();

    formData.append("file", file);

    try {

      setLoading(true);

      const response = await axios.post(
        "http://localhost:8000/upload-pdf",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setMessage(response.data.message);

    } catch {

      setMessage("Upload failed");

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="bg-white/5 border border-white/10 rounded-3xl p-6 shadow-2xl">

      <div className="flex items-center gap-3 mb-4">

        <FiUploadCloud className="text-4xl text-cyan-400" />

        <div>

          <h2 className="text-2xl font-bold">
            Upload SAP PDF
          </h2>

          <p className="text-gray-400 text-sm">
            Add SAP documents into the AI knowledge base
          </p>

        </div>

      </div>

      <div className="flex flex-col md:flex-row gap-4">

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
          className="text-white"
        />

        <button
          onClick={handleUpload}
          disabled={loading}
          className="bg-blue-600 hover:bg-blue-700 transition-all px-6 py-3 rounded-2xl font-semibold"
        >
          {loading ? "Uploading..." : "Upload PDF"}
        </button>

      </div>

      {message && (

        <div className="mt-4 text-green-400 font-semibold">
          {message}
        </div>

      )}

    </div>
  );
}