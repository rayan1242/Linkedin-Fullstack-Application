<script lang="ts">
  import { createEducation, type EducationParams } from '$lib/api/education'; // Adjust the import path as necessary

  let education: EducationParams = {
    user_id: 0,
    institution_id: 0,
    start: '',
    end: '',
    course: '',
    duration: 0
  };

  let message = '';

  const handleSubmit = async () => {
    try {
      const response = await createEducation(education);
      if (response.status === 'success') {
        message = 'Education record created successfully!';
        handleRefresh();
      } else {
        message = `Error: ${response.message}`;
      }
    } catch (error) {
      console.error(error);
      message = 'Error creating education record.';
    }
  };

  const handleRefresh = () => {
    education = {
      user_id: 0,
      institution_id: 0,
      start: '',
      end: '',
      course: '',
      duration: 0
    };
    message = '';
  };
</script>

<form on:submit|preventDefault={handleSubmit}>
  <input type="number" bind:value={education.user_id} placeholder="User ID" required />
  <input type="number" bind:value={education.institution_id} placeholder="Institution ID" required />
  <input type="date" bind:value={education.start} placeholder="Start Date" required />
  <input type="date" bind:value={education.end} placeholder="End Date" />
  <input type="text" bind:value={education.course} placeholder="Course" required />
  <input type="number" bind:value={education.duration} placeholder="Duration" required />
  <button type="submit">Create Education</button>
</form>

<button on:click={handleRefresh}>Refresh</button>

{#if message}
  <p>{message}</p>
{/if}