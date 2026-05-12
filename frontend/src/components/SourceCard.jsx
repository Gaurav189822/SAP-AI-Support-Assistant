const SourceCard = ({ source }) => {

  return (
    <div className="bg-gray-800 p-3 rounded-lg mt-2">

      <p className="text-sm text-gray-300">
        {source.chunk}
      </p>

      <p className="text-xs text-green-400 mt-2">
        Score: {source.score.toFixed(2)}
      </p>

    </div>
  );
};

export default SourceCard;