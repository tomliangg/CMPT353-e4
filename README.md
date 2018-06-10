# Movie_Title_Entity_Resolution-CMPT353_e4_p1
<h3>This repo is created for documentation purpose. The repo contains my personal work toward the SFU CMPT353 (Computational Data Science) course. You may use my solution as a reference. The .zip archive contains the original exercise files. For practice purpose, you can download the .zip archive and start working from there.</h3>

<p><a href="https://coursys.sfu.ca/2018su-cmpt-353-d1/pages/AcademicHonesty">Academic Honesty</a>: it's important, as always.</p>
<br/>
<p> You are given two files: movie_list.txt (it has a list of movie title with correct names) and movie_ratings.csv (it has the ratings and movie title with incorrect names due to misspelling or other mistakes). The task of this exercise is to find the average ratings for each movie. </p>
<br/>
<p>Below is the exercise description </p>
<hr>


<div class="wikicontents creole tex2jax_ignore"><p>Due <span title="2018-06-08T23:59:59-07:00">Friday June 08 2018</span>.</p>
<p>Some files are provided that you need below: <a href="E4.zip">E4.zip</a>. <strong>You may not write any loops</strong> in your code.</p>
<h2 id="h-movie-title-entity-resolution">Movie Title Entity Resolution</h2>
<p>For this question, we will use some movie rating data derived from the <a href="https://github.com/sidooms/MovieTweetings">MovieTweetings</a> data set.</p>
<p>The first thing you're given (<code>movie_list.txt</code> in the ZIP file) is a list of movie titles, one per line, like this:</p>
<pre class="highlight lang-plain">Bad Moms
Gone in Sixty Seconds
Raiders of the Lost Ark</pre>
<p>The second file (<code>movie_ratings.csv</code>) contains users' rating of movies: title and rating pairs. Well<span>&hellip;</span> the title, except the users have misspelled the titles.</p>
<pre class="highlight lang-plain">title,rating
Bad Mods,8
Gone on Sixty Seconds,6.5
Gone in Six Seconds,7</pre>
<p>The task for this question is to <strong>determine the average rating for each movie</strong>, compensating for the bad spelling in the ratings file. We will assume that the movie list file contains the correct spellings.</p>
<p>There are also some completely-incorrect titles that have nothing to do with the movie list. Those should be ignored. e.g.</p>
<pre class="highlight lang-plain">Uhhh some movie i watched,7</pre>
<p>Your command line should take the movie title list, movie ratings CSV, and the output CSV filename, like this:</p>
<pre class="highlight lang-bash">python3 average_ratings.py movie_list.txt movie_ratings.csv output.csv</pre>
<p>It should produce a CSV file (<code>output.csv</code> in the example above) with 'title' as the first column, and (average) 'rating' <strong>rounded to two decimal places</strong> as the second. The output should be <strong>sorted by title</strong> and include only movies with ratings in the data set.</p>
<pre class="highlight lang-plain">title,rating
Bad Moms,8.0
Gone in Sixty Seconds,6.75</pre>
<h3 id="h-hints">Hints</h3>
<ul><li>There's nothing (obvious that I see) in Pandas to read line-at-a-time input like in <code>movie_list.txt</code>. You can <code>open(movie_list).readlines()</code> to get a list of lines, and construct a DataFrame from there. Or maybe use <a href="http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_table.html">read_table</a> somehow. Using read_csv is <strong>not</strong> correct, since movie titles can contain commas.
</li><li>Finding similar strings is much easeier than I thought it was going to be: in the Python standard libarary, you'll find <a href="https://docs.python.org/3/library/difflib.html#difflib.get_close_matches">Python difflib.get_close_matches</a>. You can accept the default cutoff for what is <span>&ldquo;</span>too far<span>&rdquo;</span> to count as a match.
</li></ul>

