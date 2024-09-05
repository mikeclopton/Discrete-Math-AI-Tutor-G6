import React, { useState } from 'react';

const Input = () => {
  const [submissionType, setSubmissionType] = useState('latex');

  const handleTypeChange = (event) => {
    setSubmissionType(event.target.value);
  };

  return (
    <div>
      <h2>Input your answer here</h2>
      
      <div>
        <label>
          <input
            type="radio"
            value="latex"
            checked={submissionType === 'latex'}
            onChange={handleTypeChange}
          />
          LaTeX
        </label>
        <label>
          <input
            type="radio"
            value="photo"
            checked={submissionType === 'photo'}
            onChange={handleTypeChange}
          />
          Photo
        </label>
        <label>
          <input
            type="radio"
            value="pen"
            checked={submissionType === 'pen'}
            onChange={handleTypeChange}
          />
          Pen
        </label>
      </div>

      {submissionType === 'photo' && (
        <input type="file" placeholder="Upload a photo..." />
      )}

      {submissionType === 'pen' && (
        <textarea placeholder="Write your answer here..."></textarea>
      )}

      {submissionType === 'latex' && (
        <textarea placeholder="Enter your LaTeX code here..."></textarea>
      )}

      <button type="submit">Submit</button>
    </div>
  );
};

export default Input;
