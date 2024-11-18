<script lang="ts">
  import { createEducation, type EducationParam } from '$lib/api/education'; // Adjust the import path as necessary

  let education: EducationParam = {
    user_id: NaN,
    institution_id: NaN,
    start: '',
    end: '',
    course: '',
  };

  let message = '';


  const handleSubmit = async () => {
    try {
      // Ensure the date format is yyyy-mm-dd
      // if (!education.start || !/^\d{4}-\d{2}-\d{2}$/.test(education.start)) {
      //   message = "Start date must be provided and in 'YYYY-MM-DD' format.";
      //   return;
      // }
      education.start = new Date(education.start).toISOString().slice(0, 10);
      education.end = education.end ? new Date(education.end).toISOString().slice(0, 10) : '';

      console.log(education);

      const response = await createEducation(education);
      console.log(response);
      if (response && response.education && response.status === 'success') {
        message = 'Education record created successfully!';
      } else {
        message = `Error: ${response?.message || 'Unknown error'}`;
      }
    } catch (error) {
      console.log(error);
      message = 'Error creating education record.';
    }
  };

  const handleRefresh = () => {
    education = {
      user_id: NaN,
      institution_id: NaN,
      start: '',
      end: '',
      course: '',
    };
    message = '';
  };
</script>

<style>
  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 400px;
    margin: 10% auto;
    padding: 1rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    background-color: #f9f9f9;
  }

  input, button {
    padding: 0.5rem;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  input:focus {
    border-color: #007bff;
    outline: none;
  }

  button {
    background-color: #007bff;
    color: white;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }

  p {
    text-align: center;
    color: green;
  }
</style>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={education.user_id} placeholder="User ID" required />
  <input type="number" bind:value={education.institution_id} placeholder="Institution ID" required />
  <input type="date" bind:value={education.start} placeholder="Start Date (YYYY-MM-DD)" required />
  <input type="date" bind:value={education.end} placeholder="End Date (YYYY-MM-DD)" />
  <input type="text" bind:value={education.course} placeholder="Course ID" required />
  <button type="submit">Create Education</button>
  <button on:click={handleRefresh}>Refresh</button>
</form>

{#if message}
  <p>{message}</p>
{/if} 