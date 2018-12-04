%function H = get_wave_data;

% the address to the buoy data (should pass in as argument)
% 46053 = E. Santa Barbara
% 46054 = W. Santa Barbara
% 46217 = Anacapa Passage
% 46086 = San Clemente Basin
% 46219 = San Nicolas Island
filename = '46054'; % the buoy name
url = sprintf('https://www.ndbc.noaa.gov/data/realtime2/%s.data_spec',filename);
outfilename = websave(filename,url);

fid = fopen(outfilename);
N = 46; % this is different for different buoys
format = ['%{y}D%{m}D%{d}D%{hh}D%{mm}D%f' repmat('%f(%f)', [1 N])];
%skip one HeaderLine
c = textscan(fid, format,'HeaderLines',1);
fclose(fid);

% get frequency data (s^-1) 
% 1/seconds measure of cycles per second
n = length(c{8});
f = zeros(n,N);
for i = 1:N
    iN = 8+2*(i-1);
    f(:,i) = c{iN};
end

% get wave energy data (m^2 s)
% meters squared per second (Energy)
E = zeros(n,N); % blank array
for i = 1:N
    iN = 7+2*(i-1); % starting on the 7th col (1-based)
    E(:,i) = c{iN};
end

% calculate df and Emid 
% average of 
df = diff(f,1,2); % compare this element with the one next to it, along the 2nd dimension
Emid = .5*(E(:,1:N-1)+E(:,2:N));
fmid = .5*(f(:,1:N-1)+f(:,2:N));

% significant wave height (m -> multiply by 3.28 to get in feet)
% integrating across the entire range of frequencies
% (the integral)
SWH = 4*sqrt(sum(df.*Emid,2)); % .* takes two arrays and returns a 3rd array (of same size) The '2' restricts this to the 2nd dimension
% Why muntiply by 4?

% calculate significant wave height as a function of wave period
% 'P' is for period (second intervals)
P = [0,5,7,9,11,13,15,17,19,21,35];%25];%[5.5,6.5,7.5,8.5,9.5,10.5,11.5,13,15,19,22];
Pmid = .5*(P(1:end-1)+P(2:end)); % calculating the mid-points for each period (makes the plots nicer)
Pf = 1./fmid(1,:); % shift the focus from frequencies to periods
SWHmid = zeros(size(df, 1),length(Pmid)); % set aside space for this data set
for i = 1:length(Pmid)
    ii = find(Pf>P(i) & Pf<=P(i+1));
    SWHmid(:,i) = 4*sqrt(sum(df(:,ii).*Emid(:,ii),2)); % !!
end

% plot
w = colormap(jet(length(Pmid)));
set(groot,'defaultAxesColorOrder',w);
plot(flip(SWH(1:60))*3.28,'k','LineWidth',3)
hold on
plot(flip(SWHmid(1:60,:))*3.28,'LineWidth',1.2)
legend('Total','<5s','6s','8s','10s','12s','14s','16s','18s','20s','>20s','location','eastoutside')
set(gca,'FontSize',14)
ylabel('Significant Wave Height (ft)')
xlabel('Hours')
