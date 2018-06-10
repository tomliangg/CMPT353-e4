# CMPT353-e4
<h3>This repo is created for documentation purpose. The repo contains my personal work toward the SFU CMPT353 (Computational Data Science) course. You may use my solution as a reference. The .zip archive contains the original exercise files. For practice purpose, you can download the .zip archive and start working from there.</h3>

<p><a href="https://coursys.sfu.ca/2018su-cmpt-353-d1/pages/AcademicHonesty">Academic Honesty</a>: it's important, as always.</p>
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
<h2 id="h-cities-temperatures-and-density">Cities: Temperatures and Density</h2>
<p>This question will combine information about cities from <a href="https://www.wikidata.org/wiki/Q24639">Wikidata</a> with a different subset of the <a href="https://www.ncdc.noaa.gov/data-access/land-based-station-data/land-based-datasets/global-historical-climatology-network-ghcn">Global Historical Climatology Network</a> data.</p>
<p>The question I have is: <strong>is there any correlation between population density and temperature</strong>? I admit it's an artificial question, but one we can answer. In order to answer the question, we're going to need to get population density of cities matched up with weather stations.</p>
<p>The program for this part should be named <code>temperature_correlation.py</code> and take the station and city data files in the format provided on the command line. The last command line argument should be the filename for the plot you'll output (described below).</p>
<pre class="highlight lang-bash">python3 temperature_correlation.py stations.json.gz city_data.csv output.svg</pre>
<h3 id="h-the-data">The Data</h3>
<p>The collection of weather stations is quite large: it is given as a line-by-line JSON file that is gzipped. That is a fairly common format in the big data world. You can read this into Pandas with the built in <code>gzip</code> module and code like this:</p>
<pre class="highlight lang-python">station_fh = gzip.open(stations_filename, 'rt', encoding='utf-8')
stations = pd.read_json(station_fh, lines=True)</pre>
<p>The <code>'avg_tmax'</code> column in the weather data is <span>&deg;</span>C<span>&times;</span>10 (because that's what GHCN distributes): it needs to be divided by 10. The value is the average of TMAX values from that station for the year: the average daily-high temperature.</p>
<p>The city data is in a nice convenient CSV file. There are many cities that are missing either their area or population: we can't calculate density for those, so they can be removed. Population density is population divided by area.</p>
<p>The city area is given in m², which is hard to reason about: convert to km². There are a few cities with areas that I don't think are reasonable: exclude cities with area greater than 10000 km².</p>
<h3 id="h-entity-resolution">Entity Resolution</h3>
<p>Both data sets contain a latitude and longitude, but they don't refer to exactly the same locations. A city's <span>&ldquo;</span>location<span>&rdquo;</span> is some point near the centre of the city. That is very unlikely to be the exact location of a weather station, but there is probably one nearby.</p>
<p>Find the weather station that is closest to each city. We need it's <code>'avg_tmax'</code> value. This takes an O(mn) kind of calculation: the distance between every city and station pair must be calculated. Here's a suggestion of how to get there:</p>
<ul><li>Write a function <code>distance(city, stations)</code> that calculates the distance between <strong>one</strong> city and <strong>every</strong> station. You can probably adapt your function from the GPS question last week. [1]
</li><li>Write a function <code>best_tmax(city, stations)</code> that returns the best value you can find for <code>'avg_tmax'</code> for that one city, from the list of all weather stations. Hint: use <code>distance</code> and <code>numpy.argmin</code> (or <code>Series.idxmin</code> or <code>DataFrame.idxmin</code>) for this. [2]
</li><li>Apply that function across all cities. You can give extra arguments when applyling in Pandas like this: <code>cities.apply(best_tmax, stations=stations)</code>.
</li></ul>
<p>[1] When working on the collection of stations, make sure you're using Python operators on Series/arrays or <a href="https://docs.scipy.org/doc/numpy/reference/ufuncs.html#math-operations">NumPy ufuncs</a>, which are much faster than <code>DataFrame.apply</code> or <code>np.vectorize</code>. Your program should take a few seconds on a reasonably-fast computer, not a few minutes. [Aside: Python operators on Series/arrays are overloaded to call those ufuncs.]</p>
<p>[2] Note that there are a few cities that have more than one station at the same minimum distance. In that case, we'll use the station that is <strong>first</strong> in the input data. That choice happens to match the behaviour of <code>.argmin</code> and <code>.idxmin</code>, so if you ignore the ambiguity, you'll likely get the right result.</p>
<h3 id="h-output">Output</h3>
<p>Produce a scatterplot  of average maximum temperature against population density (in the file given on the command line).</p>
<p>Let's give some nicer labels than we have in the past: see the included <code>sample-output.svg</code>. The strings used are beautified with a couple of Unicode characters: <code>'Avg Max Temperature (\u00b0C)'</code> and <code>'Population Density (people/km\u00b2)'</code>.</p>
<h2 id="h-questions">Questions</h2>
<p>Answer these questions in a file <code>answers.txt</code>. [Generally, these questions should be answered in a few sentences each.]</p>
<ol><li>Based on your results for the last question, do you think daily temperatures are a good way to predict population density? Briefly explain why or why not.
</li><li>The larger data file (<code>stations.json.gz</code>) was kept compressed throughout the analysis. Constantly decompressing the data seems inefficient. Why might this be faster than working with the uncompressed <code>.json</code> data?
</li></ol>
<h2 id="h-submitting">Submitting</h2>
<p>Submit your files through CourSys for <a href="/2018su-cmpt-353-d1/+e4/">Exercise 4</a>.</p></div>

<div class="updateinfo">Updated Fri June 08 2018, 09:11 by ggbaker.

</div>
