const MessageBubble = ({ message, sender }) => {

  return (
    <div
      className={`p-3 rounded-xl max-w-[80%] mb-4 ${
        sender === "user"
          ? "bg-blue-600 ml-auto"
          : "bg-gray-700 mr-auto"
      }`}
    >
      {message}
    </div>
  );
};

export default MessageBubble;